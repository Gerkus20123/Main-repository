import { DataTypes } from 'sequelize';


// Model Wiadomosc
export default (sequelize) => {
  const Wiadomosc = sequelize.define('Wiadomosc', {
    content: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
  }, {
    tableName: 'Messages',
    timestamps: true,
  });

  return Wiadomosc;
};
